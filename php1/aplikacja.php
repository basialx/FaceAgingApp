<?php

 session_start();
 if(!isset($_SESSION['zalogowany']))
 {
	 header('Location: index.php');
	 exit();
 }
 
?>

<!DOCTYPE HTML>
<html lang="pl>
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <title>strona logowania</title>
</head>
<body>

<?php
 
  echo "<p>Witaj ".$_SESSION['user'].' w aplikacji FaceAgingApp [<a href="logout.php">Wyloguj sie!</a>]</p?>';
  
?>

</body>
</html>