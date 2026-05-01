<template>
  <div class="group flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 transition">
    <div class="w-9 h-9 rounded-lg bg-primary-50 text-primary-600 flex items-center justify-center shrink-0">
      <component :is="iconMap[icon]" />
    </div>
    <a
      :href="href"
      :target="external ? '_blank' : undefined"
      :rel="external ? 'noopener' : undefined"
      class="flex-1 min-w-0 text-sm text-gray-800 truncate hover:text-primary-700 transition"
    >
      {{ value }}
    </a>
    <button
      type="button"
      @click="onCopy(copyKey, value)"
      class="opacity-0 group-hover:opacity-100 focus:opacity-100 transition text-xs px-2 py-1 rounded text-gray-500 hover:text-primary-700 hover:bg-primary-50 shrink-0"
    >
      {{ copiedKey === copyKey ? copiedLabel : copyLabel }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { h } from 'vue'

defineProps<{
  icon: 'mail' | 'phone' | 'link' | 'pin'
  value: string
  href: string
  external?: boolean
  onCopy: (key: string, value: string) => void
  copyKey: string
  copyLabel: string
  copiedLabel: string
  copiedKey: string
}>()

const iconMap = {
  mail:  () => h('svg', { class: 'w-4 h-4', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z' })]),
  phone: () => h('svg', { class: 'w-4 h-4', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M3 5a2 2 0 012-2h2.5a1 1 0 01.95.68l1.5 4.5a1 1 0 01-.5 1.21L8 10.5a11 11 0 005.5 5.5l1.1-1.46a1 1 0 011.2-.5l4.5 1.5a1 1 0 01.7.95V19a2 2 0 01-2 2A16 16 0 013 5z' })]),
  link:  () => h('svg', { class: 'w-4 h-4', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1' })]),
  pin:   () => h('svg', { class: 'w-4 h-4', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M17.657 16.657L13.414 20.9a2 2 0 01-2.828 0l-4.244-4.243a8 8 0 1111.314 0z' }), h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M15 11a3 3 0 11-6 0 3 3 0 016 0z' })])
}
</script>
