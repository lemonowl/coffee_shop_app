<template>
  <div class="card mb-3" :id="order.id">
    <div class="card-header d-flex justify-content-between align-items-center">
      <span><strong>Order #{{ order.number }}</strong></span>
      <span><strong>€ {{ order.total }}</strong></span>
    </div>
    <div class="card-body">
      <ul class="list-group list-group-flush">
        <li v-for="product in order.items" :key="product.id" class="list-group-item">
          <div class="row d-flex justify-content-between align-items-center">
            <div class="col-md-10">
              <h6 class="my-0">{{ product.name }}</h6>
              <small class="text-muted">{{ product.comment }}</small>
            </div>
            <div class="col-md-1">
              <span class="text-muted">{{ product.count }}</span>
            </div>
            <div class="col-md-1">
              <span class="text-muted">$ {{ product.price }}</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div class="card-footer">
      <div class="row">
        <div class="col-md-9">
          <div>Status: <strong>{{ order.status }}</strong></div>
          <div>Comment: {{ order.comment }}</div>
        </div>
        <div class="col-md-3 d-flex justify-content-end align-items-center">
          <button class="btn btn-sm btn-secondary me-2" @click="editOrder(order.id)">Edit order</button>
          <button class="btn btn-sm btn-success" @click="completeOrder(order.id)">Complete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    order: {
      type: Object,
    }
  },
  methods: {
    editOrder(orderId) {
      this.$emit('editOrder', orderId);
    },
    completeOrder(orderId) {
      this.$emit('completeOrder', orderId);
    }
  }
};
</script>