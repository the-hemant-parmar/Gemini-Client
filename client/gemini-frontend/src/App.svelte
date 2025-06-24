<script>
  import Chat from "./lib/Chat.svelte";

  let questions = $state([]);
  let query = $state("What is the capital of India?");
  let response = $state("");

  async function onclick(){
    const output = await fetch('http://localhost:8000/predict?question='+query);
    const out_json = await output.json();
    response = out_json.answer;
    update()
    console.log($state.snapshot(questions))
  }

  function update(){
    questions.unshift({
        que:query,
        ans:response,
        id:questions.length+1 
    })
  }
</script>

<div id="content">

  <div id="left">
    
    <h2 style="color: #023047">Enter your query to ask</h2>
    
    <div id="ask">
      
      <textarea id='question' bind:value={query} >
      </textarea>
      <button {onclick}>Ask</button>
      
    </div>
  </div>
  
  <div id="right">

    {#each questions as que_obj (que_obj.id)}
    <Chat {que_obj}></Chat>
    {/each}
    
  </div>
</div>
  
  <style>
  textarea {
    height: 70px;
    min-width: 250px;
    width:100%;
    border: none;
    overflow-wrap:break-word;
    word-wrap: normal;
    padding-left: 25px;
    font-size: 1.5em;
    border-bottom-left-radius: 25px;
    border-top-left-radius: 25px;
  }
  
  button{
    min-width:100px;
    border-top-right-radius: 25px;
    border-bottom-right-radius: 25px;
    border: none;
  }

  div#left {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-width: 50%;
    width: 50%;
    background-color: #8ecae6;
  }

  div#ask {
      display: flex;
      /* flex-direction: column; */
      width: 80%;
  }

  div#right {
    max-width: 50%;
    /* width:500px; */
    /* background-color: #111111; */
    margin: auto;
  }

  div#content {
    height: 729px;
    background-color: #023047;
    display: flex;
    justify-content: space-evenly;
  }
</style>