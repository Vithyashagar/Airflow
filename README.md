# Airflow Introduction

## <span style="color:#ffbd40"> Introduction to Apache Airflow <span>

- Apache airflow is an open source platform for developing, scheduling, and monitoring batch oriented workflows.
- A web interface is available to monitor the state of the workflows.
- Airflow is scalable it can work from a laptop to distributed large system.
- It uses a <span style="color:#f57373">**workflow as a code**<span> approch.
- This helps air flow to be <span style="color:#f57373">**Dynamic**<span>, <span style="color:#f57373">**Extensible**<span> and <span style="color:#f57373">**Flexible**<span>(Workflow parameterization is built using *jinja*)
- A <span style="color:#f57373">**DAG**<span> is Airflow’s representation of a *workflow*.
- \>> Between the tasks defines a dependency and controls in which order the tasks will be executed.

### <span style="color:#ffbd40">Advantages of using Airflow<span>

- Workflows can be stored in version control so that you can roll back to previous versions
- Workflows can be developed by multiple people simultaneously
- Tests can be written to validate functionality
- Components are extensible and you can build on a wide collection of existing components

### <span style="color:#ffbd40">Why not Airflow<span>

- Airflow is not a streaming solution.
- It uses coding to do the workflows.  

### <span style="color:#ffbd40">Installation<span>

Installation in windows can be tricky. We can either use Windows Subsytem for Linux or docker image to install airflow.
- [WSL2 installation](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/)
    After installing the dependencies use below command to install ubuntu in cmd. 
    ```console
        wsl --install -d Ubuntu
    ``` 
- [Airflow Installation without docker in windows](https://www.freecodecamp.org/news/install-apache-airflow-on-windows-without-docker/)

### <span style="color:#ffbd40">Freequently used commands<span>

- To activate the environment.(Always remember to restart the terminal when storing any variables)
```console
    source airflow_env/bin/activate
```
- To go to airflow home
```console
    cd $AIRFLOW_HOME
```

- User creation
```console
airflow users create --username admin –password admin –firstname admin –lastname admin –role Admin –email youremail@email.com
```

- check created user
```console
airflow users list
```

- Run the webserver
```console
airflow scheduler 
airflow webserver 
```

or to specify the port
```console
airflow webserver –port <port number>
```

or to start in a single process
```console
airflow standalone
```
Check dag script for errors

```console
python ~/path/to/script.py
```

Metadata validation
```python
# initialize the database tables
airflow db init

# print the list of active DAGs
airflow dags list

# prints the list of tasks in the "tutorial" DAG
airflow tasks list tutorial

# prints the hierarchy of tasks in the "tutorial" DAG
airflow tasks list tutorial --tree
```

Testing in local
```python
# command layout: command subcommand [dag_id] [task_id] [(optional) date]

# testing print_date
airflow tasks test tutorial print_date 2015-06-01

# testing sleep
airflow tasks test tutorial sleep 2015-06-01

# testing templated
airflow tasks test tutorial templated 2015-06-01
```