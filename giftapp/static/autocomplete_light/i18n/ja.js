/*! Select2 4.1.0-rc.0 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(n){var e;(e=n&&n.fn&&n.fn.select2&&n.fn.select2.amd?n.fn.select2.amd:e).define("select2/i18n/ja",[],function(){return{errorLoading:function(){return"結果が読み込まれませんでした"},inputTooLong:function(n){return n.input.length-n.maximum+" 文字を削除してください"},inputTooShort:function(n){return"少なくとも "+(n.minimum-n.input.length)+" 文字を入力してください"},loadingMore:function(){return"読み込み中…"},maximumSelected:function(n){return n.maximum+" 件しか選択できません"},noResults:function(){return"対象が見つかりません"},searching:function(){return"検索しています…"},removeAllItems:function(){return"すべてのアイテムを削除"}}}),e.define,e.require},event=new CustomEvent("dal-language-loaded",{lang:"ja"});document.dispatchEvent(event);