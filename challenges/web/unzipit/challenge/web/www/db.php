<?php
$host = "172.24.99.5"; 
$user = "ctf";
$pass = "Jie2Roh8ohre3Ahn";
$db   = "ctf";


$connect = mysqli_connect($host, $user, $pass, $db);

if (!$connect) {
    die("Connection failed: " . mysqli_connect_error());
}

?>
