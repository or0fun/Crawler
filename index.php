<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
		<script src="http://apps.bdimg.com/libs/jquery.cookie/1.4.1/jquery.cookie.js"></script>
		<style type="text/css">
			body{
				text-align:left;
				margin-left: 250px;
			}
			.s_btn {
				width: 250px;
				height: 34px;
				border: 0;
				color: white;
				letter-spacing: 1px;
				background: #3385ff;
				border-bottom: 1px solid #2d78f4;
				outline: medium;
				-webkit-appearance: none;
				-webkit-border-radius: 0;
				font-size: 14px;
				cursor: pointer;
			}
			.s_ipt {
			    width: 426px;
			    height: 22px;
			    font: 16px/22px arial;
			    margin: 6px 0 0 7px;
			    padding: 0;
			    background: transparent;
			    border: 0;
			    outline: 0;
			    -webkit-appearance: none;
			}
			.from {
			    width: 126px;
			    height: 22px;
			    font: 16px/22px arial;
			    margin: 6px 0 0 7px;
			    padding: 0;
			    background: transparent;
			    border: 0;
			    outline: 0;
			    -webkit-appearance: none;
			}
			.fm {
			    clear: none;
			    margin: 11px 0 0 10px;
			}
			.s_ipt_wr {
			    border: 1px solid #b6b6b6;
			    border-color: #7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;
			    background: #fff;
			    display: inline-block;
			    vertical-align: top;
			    width: 439px;
			    height: 32px;
			    margin-right: 2;
			    border-color: #b8b8b8 #b8b8b8 #ccc #b8b8b8;
			}
			.s_ipt_from {
			    border: 1px solid #b6b6b6;
			    border-color: #7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;
			    background: #fff;
			    display: inline-block;
			    vertical-align: top;
			    width: 139px;
			    height: 32px;
			    margin-right: 10;
			    border-color: #b8b8b8 #b8b8b8 #ccc #b8b8b8;
			}
		</style>

		<script type="text/javascript">
			$(document).ready(function(){
				$("#crawler").click(function(){
					$("#msg").html("正在爬...一天的新闻平均需要0.2s");
					$.cookie('crawler_words', $("#words").val(), { expires: 365 }); 
					$.cookie('crawler_fromdate', $("#fromdate").val(), { expires: 365 }); 
					htmlobj=$.ajax({url:"crawler.php?words=" + $("#words").val() + 
						"&fromdate=" +
						$("#fromdate").val(),
						async:true,
						success: function(data){
							window.location.reload();
						}});
				});
			});
			$("#words").val($.cookie('crawler_words'));
			$("#fromdate").val($.cookie('crawler_fromdate'))
		</script>
	</head>
	<body>

	
		<br/>
		<br/>
		<br/>

		<span class="s_ipt_from">
			<input name="fromdate" id="fromdate" class="from" value="2017-02-01" maxlength="100" autocomplete="on">
		</span>
		<span class="s_ipt_wr">
			<input name="word" id="words" class="s_ipt" value="YunOS" maxlength="100" autocomplete="on">
			
		</span>
		<span class="s_btn_wr">
			<button id="crawler" class="s_btn">爬一下</button>
		</span>
		
	
		<br/>
		<br/>


		1、起始时间格式为yyyy-mm-dd，如：2016-02-03<br/>
		2、关键词，多个时以空格隔开
		<br/>
		<br/>
		<br/>
		<p id="msg" ></p>
		<br/>
		<br/>
		<br/>
		<?php

		echo "历史记录:<br/>";
		$current_dir = 'output';
		if(is_dir($current_dir)) {
			$dir = opendir($current_dir);
			while(false !== ($file=readdir($dir))){
				if($file != "." && $file != ".." && strstr($file, ".xls")){
					echo "<a href='http://ie8384.com/pudding/".$current_dir."/$file'>$file</a>";
					$ctime = filectime($current_dir."/".$file);
					echo "        Created:".date("Y-m-d H:i:s",$ctime);
					echo "<br/>";
				}
			}
			closedir($dir);
		}
		?>
	</body>
</html>