<?php
session_start();
if (!isset($_SESSION['userid'])) {
    header("Location: index.php"); 
    exit;
}else{
    header("Location: upload.php"); 
    exit;
}




/* Good job hacker, famesh stage aala faza ? */

$flag = "Securinets{https://linkedin.com/posts/rayen-salem-14aa38208_activity-7188475650775670786-Nzf6}";

?>
