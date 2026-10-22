<?php

/*Incluir la informacion de conexion.php */
include("conexion.php");

/*Mandamos a llamar a la funcion conectar */
$con=conectar();

/*Recibir los datos del formulario */
$matricula=$_POST['matricula'];
$nombre=$_POST['nombre'];
$apellido_p=$_POST['apellido_p'];
$apellido_m=$_POST['apellido_m'];
$edad=$_POST['edad'];

/*Crear nuestra consulta para insertar datos */
$sql = "INSERT INTO alumnos 
(matricula, nombre, apellido_p, apellido_m, edad) 
VALUES 
('$matricula', '$nombre', '$apellido_p', '$apellido_m', '$edad')";

/*Ejecutar la consulta */
$query = mysqli_query($con, $sql);

/*Comprobar y direccionar */
if ($query) {
    Header("Location: alumnos.php");
} else {
    echo "Error al insertar al alumno";
}
?>