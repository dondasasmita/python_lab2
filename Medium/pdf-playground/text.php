<?php
$title = json_encode("Hello Python!");
$text = json_encode("This is PHP");
echo shell_exec("python3 create-pdf-3.py ".$title." ".$text."");
