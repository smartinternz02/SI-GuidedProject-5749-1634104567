<html>
  <head>
    <title>Detect the Iceberg</title>
    <style>
	img {
  	display: block;
  	margin-left: auto;
  	margin-right: auto;
	width: 45%
	}
	

	.header {	
			top:0;	
			margin:0px;
			left: 0%;
			right: 0px;
			position: fixed;
			background: #574032;
			color: #f1e6c8;
			overflow: hidden;
			padding: 0.5%;
			font-size: 2.9vw;
			width: 100%;
			padding-left:0px;
			text-align: center;
		}
    </style>
  </head>
  <body style="background-image:url({{url_for('static',filename='images/bck.png')}});background-position: center;background-repeat: no-repeat;
			background-size: cover;">
  <div class="header">
    <div style="align:center"><b>Streaming for Iceberg Detection</b></div>
	
  </div>
	
		<div style="margin-top:12%">
			<img id="bg" class="center" src="{{ url_for('video_feed') }}">
			<!img id="bg" class="center" src="samp.png">
		</div>
	
	
	
  </body>
  
</html>