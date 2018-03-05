import gzip
import fnmatch
import shutil
import os.path

def gunzip(file_path,output_path):
    with gzip.open(file_path,"rb") as f_in, open(output_path,"wb") as f_out:
        f_out.write("Timestamp,Line ID,Direction,Journey Pattern ID,Time Frame,Vehicle Journey ID,Operator,Congestion,Lon,Lat,Delay,Block ID,Vehicle ID,Stop ID,At Stop\n")
        shutil.copyfileobj(f_in, f_out)

def recurse_and_gunzip(root):
    walker = os.walk(root)
    for root,dirs,files in walker:
        for f in files:
            if fnmatch.fnmatch(f,"*.gz"):
                file_path = "{0}\{1}".format(root, f)
                output_path = "{0}\{1}".format(root, f.replace(".gz",""))
                gunzip(file_path,output_path)


if __name__ == '__main__':
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    busGPSSamples_zip_folder = "{0}\Data\BusGPSSamples\zip".format(main_dir)
    recurse_and_gunzip(busGPSSamples_zip_folder)



