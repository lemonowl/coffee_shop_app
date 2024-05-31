<template>
  <header class="bg-brown text-white py-3">
    <div class="container d-flex justify-content-between align-items-center">
      <router-link to="/" class="no-link-decoration">
        <div class="d-flex align-items-center text-white">
          <img src="/img/logo.png" alt="Logo" class="me-3" height="50">
          <h1 class="h3 m-0">Coffee Shop</h1>
        </div>
      </router-link>
      <div>
        <p class="mb-0">Contact us:
          <a href="tel:+123456789" class="text-white no-link-decoration">+1 234 567 89</a>
        </p>
        <p class="mb-0">Email:
          <a href="mailto:info@coffeeshop.com" class="text-white no-link-decoration">info@coffeeshop.com</a>
        </p>
      </div>
    </div>
  </header>
</template>