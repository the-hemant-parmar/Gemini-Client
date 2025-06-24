<script>
    // the structure of question[i] = {question:"prashn", answer:"uttar", q_id:8}
    let {que_obj} = $props();
    
</script>

<div>
    <b><p>[{que_obj.id}] : {que_obj.que}</p></b>
    <p class="ans">  {que_obj.ans}</p>    
</div>

<style>
    .ans {
        font-size: 1.5em;
    }
</style>