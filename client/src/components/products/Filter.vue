<template>
  <aside class="col-md-3 mb-4">
    <div class="card">
      <div class="card-header">
        <h5>Filter</h5>
      </div>
      <div class="card-body">
        <div class="mb-3">
          <label for="filter-category" class="form-label">Category</label>
          <select id="filter-category" class="form-select" v-model="filter.category">
            <option value="">All</option>
            <option v-for="category in categories" :key="category" :value="category.key">
              {{ category.name }}
            </option>
          </select>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  props: {
    categories: {
      type: Array,
    },
    filter: {
      type: Object,
    },
  }
};
</script>