<?php

/*Incluir la informacion de conexion.php */
include("conexion.php");

/*Mandamos a llamar a la funcion conectar */
$con=conectar();

/*Dame todo lo que tenga alumnos */
$select="SELECT * FROM alumnos";

/*Ejecutar la consulta y tendremos acceso a la conexion */
$query=mysqli_query($con,$select);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <h1>Alumnos</h1>
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Matricula</th>
                    <th>Nombre</th>
                    <th>Apellido Paterno</th>
                    <th>Apellido Materno</th>
                    <th>Edad</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>123456</td>
                    <td>Cristopher Danilo</td>
                    <td>Hernandez</td>
                    <td>Herrera</td>
                    <td>19</td>
                    <td>Eliminar | Editar</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>