<?php
session_start();
?>
<!DOCTYPE HTML>
<html lang="pl">
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <title>GALERIA</title>
  <link href="style.css" type="text/css" rel="stylesheet"/>
</head>
<body>
 <br/><br/>
<?php
echo "<p>Galeria uzytkownika ".$_SESSION['user'].' [<a href="aplikacja.php">Powrót do menu</a>]</p?>';
?>
<br/><br/>
<br/><br/>
<?php
$directory="./galeria";
$dir=opendir($directory);
 
while($file_name=readdir($dir))
    {
         if(($file_name!=".")&&($file_name!=".."))
        {
	 echo '<img src="galeria/'.$file_name.'">';
	 echo "<br></br>";
        }
    }
 
closedir($dir);
 
?>
</body>
</html>