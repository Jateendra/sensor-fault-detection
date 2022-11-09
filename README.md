# sensor-fault-detection

This project is for early sensing if a sensor might result to faulty product or not . Based on the judgement , machanics will find and collect all the information prior to mount them in the field and do a lot of testing to reproduce or design them again . This will help the product to be more reliable and durable over the period of time . Eventually , safety terms plays a big role by the identification of early failures with the help of ML concept and application .

# Project Setup

Step 1 : Clone the Repository :

    ```
    git clone https://github.com/Jateendra/sensor-fault-detection.git
    ```

Step 2 : Create Conda environment :

    ```
    conda create -p venv python==3.8 -y
    conda activate venv/ OR source activate venv/
    ```

    Once env is setup , check on below commands :

    ```
    python ** To check if 3.8 python version is installed or not .
    pip list ** Toc check all installed libraries .
    ```

Step 3 ** : setup.py [ write code as below ] . Run command : ```python setup.py install```

    ```
    from setuptools import find_packages,setup

    setup(
        name="sensor",
        version="0.0.1",
        author="Jateendra",
        author_email="jateendra.pradhan@gmail.com",
        packages=find_packages(),, ## It tried to search for the packages in the project folder .
    )
    ```

    ** delete build , dist , sensor.egg-info folders as it's not required for now .

Step 4 : Keep creating folders and structure for the project . Then push to Git :

    ```
    git add .
    git commit -m "structure setup completed"
    git push origin main

    ```

    ** Incase user name conflicts , follow - 1 :

    ```
    git config --global user.name "Jateendra"
    git config --global user.email jateendra.pradhan@gmail.com
    git config --global user.name
    git status
    git push origin main --force
    ```

    ** Incase not able to push to github , follow -2 :

    ```
    rm -rf .git
    git init -b main
    git add .
    git commit -m "first pipeline setup"
    git remote add origin https://github.com/Jateendra/sensor-fault-detection.git
    git remote -v
    git push origin main
    git push origin main --force
    history
    ```

Step-5 : How to run the application .

```
if __name__=="__main__":
    #main()
    # set_env_variable(env_file_path)
    app_run(app, host=APP_HOST, port=APP_PORT) # To run it via Github->AWS
    # app_run(app) # To run the code locally
```    
