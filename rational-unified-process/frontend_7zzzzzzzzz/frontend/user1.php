<?php
// на какие данные рассчитан этот скрипт
header("Content-Type: application/get");
// разбираем JSON-строку на составляющие встроенной командой
$data = json_decode(file_get_contents("php://input"));
// отправляем в ответ строку с подтверждением

//{"name": name.value, "workerid": workerid.value,"wage":wage.value,"password":password.value,"role":role.value});
echo json_encode(array("name" => $data->name, "workerid" => $data->workerid,
    "wage" => $data->wage,"password" => $data->password,"role" => "admin"));