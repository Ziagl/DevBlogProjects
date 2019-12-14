<?php
	$url = "http://www.developer-blog.net";
	
	print_r(find_all_links($url));
	
	function find_all_links($url)
	{
		$htmlData = file_get_contents($url);
		if(preg_match_all('/<a\s+href=["\']([^"\']+)["\']/i', $htmlData, $links, PREG_PATTERN_ORDER))
		{
    		return array_unique($links[1]);
		}
		return null;
	}
?>