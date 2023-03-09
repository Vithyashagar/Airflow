from datetime import datetime, timedelta
from textwrap  import dedent
from airflow import DAG # The DAG object to instantiate DAG
from airflow.operators.bash import BashOperator

