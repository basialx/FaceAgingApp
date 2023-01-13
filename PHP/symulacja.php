<?php

  $tmp_name = $_FILES["plik"]["tmp_name"];
  $name = basename($_FILES["plik"]["name"]);
  move_uploaded_file($tmp_name, "galeria/".$name);

?>
<!DOCTYPE HTML>
<html lang="pl">
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <title>FaceAgingApp</title>
  <link href="style.css" type="text/css" rel="stylesheet"/>
</head>
<body>
<br/><br/>
  O to twoja wykonana symulacja ;) 
<br/><br/>
<?php
  echo '<img src="galeria/'.$name.'">';
?>
 <br/><br/>
 <a href ="aplikacja.php"> Wykonaj ponownie </a>
</body>
</html>
