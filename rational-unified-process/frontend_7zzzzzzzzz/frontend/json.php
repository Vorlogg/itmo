<?php

header("Content-Type: application/json");

$data = json_decode(file_get_contents("php://input"));



echo json_encode(array("result" => "true", "admin" => "true","userid"=>"1"));
//elseif ($data->type == "2"):
//    echo json_encode(array("role" => "admin"));

?>
