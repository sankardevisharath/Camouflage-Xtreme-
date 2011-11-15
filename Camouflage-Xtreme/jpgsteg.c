#include <stdio.h>
#include <jpeglib.h>

struct jpeg_decompress_struct srcinfo;
j_decompress_ptr src;
struct jpeg_compress_struct dstinfo;
jvirt_barray_ptr * dct;
JBLOCKARRAY s;
struct jpeg_error_mgr jsrcerr, jdsterr;
FILE * fp, *fp1;
int i, j, k, rest = 0, err = 1, dat_len = 0, ch = 0;
long sz = 0;
jpeg_component_info *compptr;


int embed_data(char *datafile)
{
    fp1 = fopen(datafile, "r");
    fseek(fp1, 0L, SEEK_END);
    sz = ftell(fp1);
    fseek(fp1, 0L, SEEK_SET);
    for(k = 0 ; k < compptr->height_in_blocks - 1 ; k++)
        for(i = 0 ; i < compptr->width_in_blocks - 1 ; i++)
            for(j = 0 ; j < 64 ; j++)
                if(*(*(*(s + k) + i) + j) > 3 || *(*(*(s + k) + i) + j) < -4)
                    if((dat_len++) < 10)
                    {
                        *(*(*(s + k) + i) + j) = ((*(*(*(s + k) + i) + j) >> 2) << 2) | (sz % 4);
                        sz >>= 2;
                    }
                    else
                    {
                        if(rest == 0)
                        {            
                            if((ch = fgetc(fp1)) == EOF)
                            {
                                err = 0;
                                i = j = k = 0x6FFF; break;
                            }
                            rest = 4;
                        }
                        *(*(*(s + k) + i) + j) = ((*(*(*(s + k) + i) + j) >> 2) << 2) | (ch % 4);
                        ch >>= 2; rest--;
                    }
    fclose(fp1);
    return err;
}


void extract_data(char *datafile)
{
    fp1 = fopen(datafile, "w");
    for(k = 0 ; k < compptr->height_in_blocks - 1 ; k++)
        for(i = 0 ; i < compptr->width_in_blocks - 1 ; i++)
            for(j = 0 ; j < 64 ; j++)
                if(*(*(*(s + k) + i) + j) > 3 || *(*(*(s + k) + i) + j) < -4)
                    if((dat_len++) < 10)
                        sz += (*(*(*(s + k) + i) + j) ^ ((*(*(*(s + k) + i) + j) >> 2) << 2)) << ((dat_len - 1) * 2);
                    else if(sz > 0)
                    {
                        ch += (*(*(*(s + k) + i) + j) ^ ((*(*(*(s + k) + i) + j) >> 2) << 2)) << (rest++ * 2);
                        if(rest == 4)
                        {
                            fputc(ch, fp1);
                            sz--;  ch = rest = 0;
                        }
                    }
                    else { i = j = k = 0x6FFF; break; }
    sz = ftell(fp);
    fclose(fp1);
    truncate (datafile, ((sz /16) * 16));
}


main (int argc, char **argv)
{
    srcinfo.err = jpeg_std_error(&jsrcerr);
    jpeg_create_decompress(&srcinfo);
    dstinfo.err = jpeg_std_error(&jdsterr);
    jpeg_create_compress(&dstinfo);
    fp = fopen(argv[2], "r");
    jpeg_stdio_src(&srcinfo, fp);
    (void) jpeg_read_header(&srcinfo, 1);
    dct = jpeg_read_coefficients(&srcinfo);
    jpeg_copy_critical_parameters(&srcinfo, &dstinfo);
    fclose(fp);
    src = &srcinfo;
    compptr = src->comp_info;
    s = (*src->mem->access_virt_barray)((j_common_ptr) src, *dct, 0, compptr->v_samp_factor, 1);
    if(!strcmp(argv[1], "-e"))
    {   
        err = embed_data(argv[3]);
        fp = fopen(argv[4], "w");
        jpeg_stdio_dest(&dstinfo, fp);
        jpeg_write_coefficients(&dstinfo, dct);
        jpeg_finish_compress(&dstinfo);
        jpeg_destroy_compress(&dstinfo);
        (void) jpeg_finish_decompress(&srcinfo);
        jpeg_destroy_decompress(&srcinfo);
        fclose(fp);
        return err;
    }
    else if(!strcmp(argv[1], "-d"))
        extract_data(argv[3]);
}
