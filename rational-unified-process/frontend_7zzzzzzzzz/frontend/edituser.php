<?php
// на какие данные рассчитан этот скрипт
header("Content-Type: application/get");
// разбираем JSON-строку на составляющие встроенной командой
$data = json_decode(file_get_contents("php://input"));
// отправляем в ответ строку с подтверждением

//{"name": name.value, "workerid": workerid.value,"wage":wage.value,"password":password.value,"role":role.value});
echo json_encode(array("name" => "ivan", "workerid" => "752",
    "wage" => "558","password" => "7583","role" => "admin"));