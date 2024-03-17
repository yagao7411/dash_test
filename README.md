This project is to setup a dash app that is running in GCP. 
Steps are

1. setup files in the cluster driver VM	or any VM (such as by VertexAI notebook)
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
			
2	deploy the app		
	under the project folder, we run ssh:		
	gcloud app deploy	
        if permisson issue happens
        gcloud auth login	
	the url will be		
	https://ya-test-dot-gcp-wow-finance-faa-dev.ts.r.appspot.com		
	if anything went wrong, we check log, by typing:		
	gcloud app logs tail -s default		
