enable_toast = "true" # "true" or "false"
toast_msg_id = 1 # must increment when creating a new message
toast_title = "Ether Alpha's Gitcoin grant is live!"
toast_msg = "This round runs until November 30th. If you enjoy this or <a href='https://etheralpha.org/' target='_blank'>other tools</a> created, please support to help maintain existing projects and fund new ones." # Best when under 100 characters
toast_link = "https://explorer.gitcoin.co/#/round/424/0xd4cc0dd193c7dc1d665ae244ce12d7fab337a008/0xd4cc0dd193c7dc1d665ae244ce12d7fab337a008-20" # Optional, leave blank to omit
toast_link_text = "Donate"
toast_expiration = 1701302399 # epoch time in seconds


toast_css = r"""
	<style type="text/css">
		.toast-container {
			z-index: 1090;
		}
		.toast {
			border-radius: 0.5rem !important;
			background-color: var(--bs-body-bg);
		}
		.toast-header {

		}
		.toast-badge {
			height: 17px;
			width: 17px;
		}
	</style>
	"""

toast_link_html = ""
if toast_link:
	toast_link_html = f"""
		<div class="toast-buttons d-flex gap-2 mt-2 pt-2">
			<a href="{toast_link}" target="_blank" class="btn btn-dark btn-sm">{toast_link_text}</a>
			<button type="button" class="btn btn-outline-dark btn-sm" data-bs-dismiss="toast" onclick="hidetoast()">Close</button>
		</div>
		"""

toast_js = f"""
	<script type="text/javascript">
		const toastEl = document.getElementById('toast');
		const toast = new bootstrap.Toast(toastEl);
		showtoast();

		// Loads/shows notification bar if users hasn't closed it yet
		function showtoast() {{
		    if ({enable_toast} == true) {{
		        const toastName = "toast-{toast_msg_id}";
		        const hideToast = localStorage.getItem(toastName);
		        const timestamp = Math.round(Date.now()/10000)*10;
		        if (hideToast != "true" && timestamp < {toast_expiration}) {{
		            toast.show();
		        }}
		    }}
		}}
		// Hides toast bar when user closes it
		function hidetoast(id=null) {{
		    if (id) {{
		        const toastName = `toast-${{id}}`;
		        const timestamp = Math.round(Date.now()/10000)*10;
		        localStorage.setItem(toastName, timestamp);
		    }} else {{
		        const toastName = "toast-{toast_msg_id}";
		        localStorage.setItem(toastName, "true");
		    }}
		}}
	</script>
	"""

toast_html = f"""
	{toast_css}
	<!-- Toast -->
	<div class="toast-container position-fixed bottom-0 end-0 p-3">
		<div id="toast" class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-bs-autohide="false">
		    <div class="toast-header">
				<span class="toast-badge bg-info rounded-1"></span>
				<strong class="toast-title me-auto ms-2">{toast_title}</strong>
				<button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" onclick="hidetoast()"></button>
		    </div>
		    <div class="toast-body">
				<div class="toast-text">
					{toast_msg}
				</div>
				{toast_link_html}
		    </div>
		</div>
	</div>
	{toast_js}
	"""

def toast():
	if enable_toast:
		return toast_html
