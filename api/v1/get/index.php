<?php
    
    #request:  ?viewCount=1000&likeCount=1000&dislikeCount=109&favoriteCount=1030&commentCount=192         
    header('Access-Control-Allow-Origin: *');
    if(isset($_GET["viewCount"]) && isset($_GET["likeCount"]) && isset($_GET["dislikeCount"]) && isset($_GET["favoriteCount"]) && isset($_GET["commentCount"]))
    {
        $params = new \stdClass();
        $params->viewCount = $_GET["viewCount"];
        $params->likeCount = $_GET["likeCount"]; 
        $params->dislikeCOunt = $_GET["dislikeCount"]; 
        $params->favoriteCount = $_GET["favoriteCount"];
        $params->commentCount = $_GET["commentCount"]

        
        // $command = ('python C:\xampp\htdocs\api\v1\get\engine\engine.py ' . $params->id . " " . $params->momentum . " " . $params->proficiency . " ". $params->difficulty . " " .  $params->percent);
        // $output = shell_exec($command);

        $data = new \stdClass();
        $data->predictedViews = 1000

        echo json_encode($data);
        http_response_code(200);
    }else
    {
        error("error, enter the correct params");
        http_response_code(406);
    }

    function error($message)
    {
        $data = new \stdClass();
        $data->message = $message;
        echo json_encode($data);
    }
?>