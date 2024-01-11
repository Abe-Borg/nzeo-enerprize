// Initializes the Shopify Draggable library on Checklist elements.

import jQuery from 'jquery';
import Draggable from '@shopify/draggable/lib/draggable';
import SwapAnimation from '@shopify/draggable/lib/plugins';
import mrUtil from './util';

const mrAutoWidth = (($) => {
  class AutoWidth {
    constructor(element, options) {
      this.element = element;
      const elementStyle = window.getComputedStyle(this.element);
      // prettier-ignore
      this.elementCssText = `box-sizing:${elementStyle.boxSizing}
                          ;border-left:${elementStyle.borderLeftWidth} solid red           
                          ;border-right:${elementStyle.borderRightWidth} solid red
                          ;font-family:${elementStyle.fontFamily}
                          ;font-feature-settings:${elementStyle.fontFeatureSettings}
                          ;font-kerning:${elementStyle.fontKerning}
                          ;font-size:${elementStyle.fontSize}
                          ;font-stretch:${elementStyle.fontStretch}
                          ;font-style:${elementStyle.fontStyle}
                          ;font-variant:${elementStyle.fontVariant}
                          ;font-variant-caps:${elementStyle.fontVariantCaps}
                          ;font-variant-ligatures:${elementStyle.fontVariantLigatures}
                          ;font-variant-numeric:${elementStyle.fontVariantNumeric}
                          ;font-weight:${elementStyle.fontWeight}
                          ;letter-spacing:${elementStyle.letterSpacing}
                          ;margin-left:${elementStyle.marginLeft}
                          ;margin-right:${elementStyle.marginRight}
                          ;padding-left:${elementStyle.paddingLeft}
                          ;padding-right:${elementStyle.paddingRight}
                          ;text-indent:${elementStyle.textIndent}
                          ;text-transform:${elementStyle.textTransform};`;

      this.GHOST_ELEMENT_ID = '__autosizeInputGhost';

      element.addEventListener('input', AutoWidth.passWidth);
      element.addEventListener('keydown', AutoWidth.passWidth);
      element.addEventListener('cut', AutoWidth.passWidth);
      element.addEventListener('paste', AutoWidth.passWidth);

      this.extraPixels = (options && options.extraPixels) ? parseInt(options.extraPixels, 10) : 0;
      this.width = AutoWidth.setWidth(this);

      // Set `min-width` only if `options.minWidth` was set, and only if the initial
      // width is non-zero.
      if (options && options.minWidth && this.width !== '0px') {
        this.element.style.minWidth = this.width;
      }
    }

    static setWidth(input) {
      const string = input.element.value || input.element.getAttribute('placeholder') || '';
      // Check if the `ghostElement` exists. If no, create it.
      const ghostElement = document.getElementById(input.GHOST_ELEMENT_ID)
        || input.createGhostElement();
      // Copy all width-affecting styles to the `ghostElement`.
      ghostElement.style.cssText += input.elementCssText;
      ghostElement.innerHTML = AutoWidth.escapeSpecialCharacters(string);
      // Copy the width of `ghostElement` to `element`.
      let { width } = window.getComputedStyle(ghostElement);
      width = Math.ceil(width.replace('px', '')) + input.extraPixels;
      /* eslint-disable no-param-reassign */

      input.element.style.width = `${width}px`;
      return width;
    }

    static passWidth(evt) {
      const input = $(evt.target).data('autoWidth');
      AutoWidth.setWidth(input);
    }

    static mapSpecialCharacterToCharacterEntity(specialCharacter) {
      const characterEntities = {
        ' ': 'nbsp',
        '<': 'lt',
        '>': 'gt',
      };

      return `&${characterEntities[specialCharacter]};`;
    }

    static escapeSpecialCharacters(string) {
      return string.replace(/\s/g, '&nbsp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    // Create `ghostElement`, with inline styles to hide it and ensure that the text is all
    // on a single line.
    createGhostElement() {
      const ghostElement = document.createElement('div');
      ghostElement.id = this.GHOST_ELEMENT_ID;
      ghostElement.style.cssText = 'display:inline-block;height:0;overflow:hidden;position:absolute;top:0;visibility:hidden;white-space:nowrap;';
      document.body.appendChild(ghostElement);
      return ghostElement;
    }
  }

  $(document).ready(() => {
    const checklistItems = document.querySelectorAll('form.checklist .custom-checkbox div input');

    if (checklistItems) {
      mrUtil.forEach(checklistItems, (index, item) => {
        $(item).data('autoWidth', new AutoWidth(item, { extraPixels: 3 }));

        item.addEventListener('keypress', (evt) => {
          if (evt.which === 13) {
            evt.preventDefault();
          }
        });
      });
    }
  });

  return AutoWidth;
})(jQuery);

const mrChecklist = {
  sortableChecklists: new Draggable.Sortable(document.querySelectorAll('form.checklist, .drop-to-delete'), {
    plugins: [SwapAnimation],
    draggable: '.checklist > .row',
    handle: '.form-group > span > i',
  }),
};

export { mrChecklist, mrAutoWidth };
