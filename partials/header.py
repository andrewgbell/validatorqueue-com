def header(current_time):
  return f"""
    <div class="py-3 my-2 text-center">
    	<h1 class="display-5 fw-bold text-capitalize mt-2">Ethereum Validator Queue</h1>
    	<div class="col-md-10 col-lg-6 mx-auto lead mb-3 text-muted">
    		<small class="d-block fs-6">
    			Data provided by 
    			<a href="https://beaconcha.in/" target="_blank">beaconcha.in</a>
    		</small>
    		<small id="lastUpdated" class="d-block fst-italic fs-6" data-last-updated="{current_time}"></small>
    	</div>
    </div>
  """
