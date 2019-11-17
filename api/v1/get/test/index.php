<?php

    //headers
    header('Access-Control-Allow-Origin: *');

    if(isset($_GET["id"]) && isset($_GET["momentum"]) && isset($_GET["proficiency"]) && isset($_GET["difficulty"]) && isset($_GET["percent"]))
    {
        $params = new \stdClass();
        $params->id = $_GET["id"];
        $params->momentum = $_GET["momentum"];
        $params->proficiency = $_GET["proficiency"]; 
        $params->difficulty = $_GET["difficulty"]; 
        $params->percent = $_GET["percent"];
        echo json_encode($params);
        http_response_code(200);
    }else
    {
        error("enter 5 valid parameters: momentum, proficiency, difficulty, percent, and jump");
        http_response_code(406);
    }

    function error($message)
    {
        $data = new \stdClass();
        $data->message = $message;
        echo json_encode($data);
    }
?>