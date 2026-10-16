<?php

    /*Creamos una funcion */
    function conectar() {
        /*Informacion del servidor*/
        $host="localhost";
        $user="root";
        $pass="";

        /*Base de datos */
        $db="aw221";


        /*Permitir conectarnos a MySQL */
        $con=mysqli_connect($host,$user,$pass);

        /*Le vamos a decir que BD y la informacion */
        mysqli_select_db($con,$db);

        return $con;   
        

    }

?>