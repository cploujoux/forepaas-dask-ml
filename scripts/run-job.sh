echo 1
dask-scheduler --port "8786" --bokeh-port "8787" &
echo 2
mc alias set myminio http://138.195.243.174:9000 minioadmin minioadmin
echo 3
mc cp myminio/mybucket/thetest.py ./test.py
echo 4
python ./test.py
echo 5
mc cp ./output.txt myminio/mybucket/outputs/joboutput.txt
echo 6
kill %1
echo 7       


   command: ["/bin/sh", "-c"]
          args: 
            - echo 1 && dask-scheduler --port "8786" --bokeh-port "8787" & && echo 2 && mc alias set myminio http://138.195.243.174:9000 minioadmin minioadmin && echo 3 && mc cp myminio/mybucket/thetest.py ./test.py && echo 4 && python ./test.py && echo 5 && mc cp ./output.txt myminio/mybucket/outputs/joboutput.txt && echo 6 && kill %1 && echo 7