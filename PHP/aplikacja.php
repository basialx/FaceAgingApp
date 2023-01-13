<?php

 session_start();
 if(!isset($_SESSION['zalogowany']))
 {
	 header('Location: index.php');
	 exit();
 }
 if (isset($_POST["submit"])) 
 {
   $tmp_name = $_FILES["plik"]["tmp_name"];
   $name = basename($_FILES["plik"]["name"]); 
   } 
?>

<!DOCTYPE HTML>
<html lang="pl">
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <title>FaceAgingApp</title>
  <link href="style.css" type="text/css" rel="stylesheet"/>
  <style>
   .error
   {
	   color:red;
	   margin-top:10px;
	   margin-bottom:10px;
   }
  </style>
</head>
<body>
<br/><br/>
<?php
 echo "<p>Witaj _".$_SESSION['user'].'_ w aplikacji FaceAgingApp [<a href="logout.php">Wyloguj sie!</a>]</p?>';
?>

<br/><br/>
<form action="symulacja.php" method="post" enctype="multipart/form-data">
   <input type="file" name="plik">
   <input type="submit" name="submit">
</form>
<br/><br>

</body>
</html>
