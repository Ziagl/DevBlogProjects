<?php
	$url = "http://www.developer-blog.net";
	
	$mysqli = new mysqli("127.0.0.1", "root", "","test");
	if($mysqli->connect_error){
	    echo "unable to connect to Database: ".mysqli_connect_error()."\n";
	    exit();
	}

	$links = find_all_links($url);
	links_to_db($links, $mysqli);
	
	function find_all_links($url)
	{
		$htmlData = file_get_contents($url);
		if(preg_match_all('/<a\s+href=["\']([^"\']+)["\']/i', $htmlData, $links, PREG_PATTERN_ORDER))
		{
    		return array_unique($links[1]);
		}
		return null;
	}
	
	function links_to_db($links, $mysql)
	{
		//urls to db
		foreach($links as $link){
			$allowed = true;
			
			//check if url exists
			$statement = "SELECT * FROM `links` WHERE link = ?";
	        if($stmt = $mysql->prepare($statement)){
	            $stmt->bind_param("s", $link);
	            $stmt->execute();
	            $stmt->store_result();
	            if($stmt->num_rows>0){
	                $allowed=false;
	            }
	            $stmt->close();
	        }
	        
	        //insert into DB
	        if($allowed){
	        	$statement = "INSERT INTO `links` (link) VALUES (?)";
	            if($stmt = $mysql->prepare($statement)){
	                $stmt->bind_param("s", $link);
	                $stmt->execute();
	                $stmt->close();
	            }
	        }
		}
	}
?>