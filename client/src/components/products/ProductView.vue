<template>
  <div class="card h-100 d-flex flex-column">
    <img :src="product.img_path" class="card-img-top product-image" alt="Product image">
    <div class="card-body">
      <h5 class="card-title">{{ product.name }}</h5>
      <p class="card-text">{{ product.description }}</p>
      <p class="card-text"><strong>€ {{ product.price }}</strong></p>
      <p class="card-text"><em>{{ product.portion }}</em></p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
    },
  }
};
</script>