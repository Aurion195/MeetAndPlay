<script>
  import Form from "@svelteschool/svelte-forms";
  let values;
</script>

<section class="section Login">
  <Form bind:values>
      <div class="input-field col s6">
        <i class="material-icons prefix">account_circle</i>
        <input
        placeholder="Username ..."
        type="text"
        name="firstName" />
      </div>
      <div class="input-field col s6">
        <i class="material-icons prefix">lock</i>
        <input
        placeholder="Password ..."
        type="text"
        name="lastName" />
      </div>
  </Form>
</section>

<style>
  .section Login {
    margin: 25% auto;
  }
</style>