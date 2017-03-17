<template>
	<div id="welcome-container">
		<div class="card text-center">
		  <div class="card-header">
		    <h2>Blooming Garden</h2>
		  </div>
		</div>
	</div>
</template>

<script>
	export default {
	  name: 'welcome-view',
	  mounted() {
	  	console.log('welcome view loaded succesfull');
	  }
	}
</script>

<style scoped>
	#welcome-container {
		display: flex;	
		align-items: center;
		justify-content: center;
		height: 100%;
	}

	.material-icons {
		font-size: 50px;
		padding: 10px;
	}

</style>
