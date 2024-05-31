<template>
  <Header />
  <div class="container mt-4">
    <div class="row">
      <ProductFilter :categories="categories" :filter="filter" />
      <section class="col-md-9">
        <div class="row">
          <div v-if="filteredProducts.length == 0" class="col-12 mt-3 text-center">
            <h5>No products available.</h5>
          </div>
          <div v-for="product in filteredProducts" :key="product.id" class="col col-md-4 mb-4">
            <ProductView :product="product" />
          </div>
        </div>
      </section>
    </div>
  </div>
  <Footer />
</template>

<script>
import ProductFilter from './Filter.vue'
import ProductView from './ProductView.vue'

export default {
  components: {
    ProductFilter,
    ProductView,
  },
  data() {
    return {
      filter: { category: '' },
      categories: [],
      products: [],
    };
  },
  computed: {
    filteredProducts() {
      return this.products.filter(product => {
        return (!this.filter.category || product.category === this.filter.category);
      });
    }
  },
  methods: {
    getCategories() {
      this.$axios.post('/api/categories/get_list')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    },
    getProducts() {
      this.$axios.post('/api/products/get_list')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    }
  },
  mounted() {
    this.getCategories();
    this.getProducts();
  }
};
</script>