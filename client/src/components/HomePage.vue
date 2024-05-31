<template>
  <Header />
  <div class="container main mt-4 flex-grow-1">
    <h2 class="text-center mb-4">Choose section</h2>
    <div class="row justify-content-center">
      <div class="col-md-auto mb-2">
        <router-link to="/products/" class="btn btn-outline-dark">
          <strong>Digital showcase</strong>
        </router-link>
      </div>
      <div class="col-md-auto mb-2">
        <router-link to="/orders/" class="btn btn-outline-dark">
          <strong>Orders management</strong>
        </router-link>
      </div>
    </div>
  </div>
  <Footer />
</template>