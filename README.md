# root-brc-1024
Root BRC-1024 Json generator

## Usage
```
python ./random_json_generator.py Humanoid_Frostborn.json 1   
```
The first argument is the race template file, second argument is the number of json files to be generated.
The generated json file will be named as the template file name with a random number appended to it and will be saved in the generated_json folder.

第一个参数是种族模板文件名，第二个参数是你想生成的json数量，种族模板文件在http://168.119.10.254:8001/Humanoid_Abyssian.json 下载，可以自行下载想要的种族模板文件，然后修改第一个参数即可。
生成的json文件会以种族模板文件名为前缀，加上一个随机数，保存在generated_json文件夹中。