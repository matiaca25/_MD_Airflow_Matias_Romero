from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def ejecutar_tarea_python():
    print(
        "El ejecutor de Python funciona correctamente y la base de datos registra el estado!"
    )
    return "Prueba exitosa"


with DAG(
    dag_id="dag_de_prueba_v1",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["prueba"],
) as dag:
    tarea_bash = BashOperator(
        task_id="saludo_bash",
        bash_command='echo "El Scheduler detectó la tarea e inició la ejecución!"',
    )

    tarea_python = PythonOperator(
        task_id="ejecutar_python",
        python_callable=ejecutar_tarea_python,
    )

    tarea_bash >> tarea_python