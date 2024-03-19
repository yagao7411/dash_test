This project is to setup a web app that is running in GCP. 

1) Dash app, deployed in VM

1.1) setup files in the cluster driver VM	or any VM (such as by VertexAI notebook)
	under the project folder, we have:		
		main.py	# entry point to run dash
		under main.py, we give the server name and port number	
		if __name__ == '__main__':	
		    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)	
			
		app.yaml	# tells GCP how to create the application, excat this file name
		service: ya-test	
		runtime: python38
			
		basic_scaling:	
		    max_instances: 2	
		    idle_timeout: 10m	
			
		resources:	
		    cpu: 1	
		    memory_gb: 1	
		    disk_size_gb: 10	
			
		entrypoint: gunicorn -b 0.0.0.0:8080 main:server	
			
		requirements.txt	# tells GCP what lib to install, with version, exact this file name
			
1.2)	deploy the app		
	under the project folder, we run ssh:		
	gcloud app deploy	
        if permisson issue happens
        gcloud auth login	
	the url will be		
	https://ya-test-dot-gcp-wow-finance-faa-dev.ts.r.appspot.com		
	if anything went wrong, we check log, by typing:		
	gcloud app logs tail -s default		

2)streamlit app, depoyed in Cloud Run
Steps:
 2.1) to to Google Shell,
 2.2) make a subfolder of "app"
 2.3) upload Dockerfile and requirements.txt under "app" folder
 2.4) run linux commands in "linux commands.txt"
 2.5) "https://genai-yg-vecrmjfrba-ts.a.run.app/" is the link of the app, this url will show in linux outputs as well.
