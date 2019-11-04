import Vue from "vue";

const MAPPING = {
  // Interactive
  button: () => import("./Button.vue"),
  select: () => import("./Select.vue"),
  checkbox: () => import("./Checkbox.vue"),
  slider: () => import("./Slider.vue"),
  "range-slider": () => import("./RangeSlider.vue"),

  // Noninteractive
  p: () => import("./Paragraph.vue"),
  h1: () => import("./H1.vue"),
  h2: () => import("./H2.vue"),
  h3: () => import("./H3.vue"),

  // Flow control
  "container-fluid": () => import("./Container.vue"),
  row: () => import("./Row.vue"),
  column: () => import("./Column.vue"),
  hcenter: () => import("./Hcenter.vue"),
  "flexbox-line": () => import("./FlexboxLine.vue"),

  // Plots
  svg: () => import("./SVG.vue"),
};

export default Vue.component("layout-element", {
  functional: true,
  props: {
    layout: {
      type: Object,
      required: true
    }
  },
  render: function(createElement, context) {
    function mapTypeToComponent() {
      const type = context.props.layout.type;
      return MAPPING[type];
    }
    return createElement(
      mapTypeToComponent(),
      {
        props: {
          meta: context.props.layout.meta,
          children: context.props.layout.children
        }
      },
      context.children
    );
  }
});
