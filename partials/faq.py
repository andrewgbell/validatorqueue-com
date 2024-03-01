faq = r"""
	<div class="accordion mx-1 mt-4" id="accordionFaq">
		<div class="accordion-item">
			<h2 class="accordion-header">
				<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">FAQ</button>
			</h2>
			<div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFaq">
				<div class="accordion-body">
					<p class="fw-bold text-decoration-underline mb-2">What is the validator queue?</p>
					<p>Ethereum's enterance and exit queues are validators waiting to begin staking or to unstake. The network has a rate limit on how many validators can be processed per epoch (referred to as churn). If more validators are trying to enter or exit than can be processed, then they are placed in the respective queue.</p>

					<p class="fw-bold text-decoration-underline mb-2">Why is there a queue?</p>
					<p>Ethereum's enter and exit queues are mechanisms to protect the stability of Ethereum's proof of stake (PoS) consensus.</p>

					<p class="fw-bold text-decoration-underline mb-2">Will the queue go away or always be this long?</p>
					<p>If validators are joining the entrance or exit queues at a faster rate than the churn (how quickly they're processed), then the queue and wait times will increase. If no more validators join the cue, or less join than the churn rate, then the queue and wait times will decrease.</p>

					<p class="fw-bold text-decoration-underline mb-2">What is churn?</p>
					<p>The churn is a rate limit on the amount of validators that can enter or exit per epoch and <a href="https://docs.ethstaker.cc/ethstaker-knowledge-base/staking-glossary#validator-queue" target="_blank">changes based on the amount of active validators</a>. This throttling mechanism help prevent instability in consensus.</p>

					<p class="fw-bold text-decoration-underline mb-2">What is an epoch?</p>
					<p>An epoch is a period of 32 slots where the validators propose and attest for blocks. With each slot being 12 seconds, an epoch is 6.4 minutes (6 minutes and 24 seconds).</p>

					<p class="fw-bold text-decoration-underline mb-2">What is sweep?</p>
					<p>The "sweep delay" is how long it will take (after getting through the exit queue) for your funds to be withdrawn to your withdrawal address. When you exit your validator and it make it through the exit queue (if any), it becomes withdrawable. From there, the network cycles through withdrawable validators to "sweep" the balance to the specified withdrawal addresses. The more validators there are, the longer it will take to cycle through the entire set.</p>
				</div>
			</div>
		</div>
	</div>
"""
