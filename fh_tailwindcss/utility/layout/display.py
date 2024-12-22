from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/display

class Display(TailwindEnum):
    """
    Enum class representing different display utilities for Tailwind CSS.

    Attributes:
        BLOCK (str): Sets the element's display to block.
        INLINE_BLOCK (str): Sets the element's display to inline-block.
        INLINE (str): Sets the element's display to inline.
        FLEX (str): Sets the element's display to flex.
        INLINE_FLEX (str): Sets the element's display to inline-flex.
        TABLE (str): Sets the element's display to table.
        INLINE_TABLE (str): Sets the element's display to inline-table.
        TABLE_CAPTION (str): Sets the element's display to table-caption.
        TABLE_CELL (str): Sets the element's display to table-cell.
        TABLE_COLUMN (str): Sets the element's display to table-column.
        TABLE_COLUMN_GROUP (str): Sets the element's display to table-column-group.
        TABLE_FOOTER_GROUP (str): Sets the element's display to table-footer-group.
        TABLE_HEADER_GROUP (str): Sets the element's display to table-header-group.
        TABLE_ROW_GROUP (str): Sets the element's display to table-row-group.
        TABLE_ROW (str): Sets the element's display to table-row.
        FLOW_ROOT (str): Sets the element's display to flow-root.
        GRID (str): Sets the element's display to grid.
        INLINE_GRID (str): Sets the element's display to inline-grid.
        CONTENTS (str): Makes the element's children part of the parent’s layout (removes the element's box).
        LIST_ITEM (str): Sets the element's display to list-item.
        HIDDEN (str): Hides the element (display: none).
    """
    BLOCK = "block"
    INLINE_BLOCK = "inline-block"
    INLINE = "inline"
    FLEX = "flex"
    INLINE_FLEX = "inline-flex"
    TABLE = "table"
    INLINE_TABLE = "inline-table"
    TABLE_CAPTION = "table-caption"
    TABLE_CELL = "table-cell"
    TABLE_COLUMN = "table-column"
    TABLE_COLUMN_GROUP = "table-column-group"
    TABLE_FOOTER_GROUP = "table-footer-group"
    TABLE_HEADER_GROUP = "table-header-group"
    TABLE_ROW_GROUP = "table-row-group"
    TABLE_ROW = "table-row"
    FLOW_ROOT = "flow-root"
    GRID = "grid"
    INLINE_GRID = "inline-grid"
    CONTENTS = "contents"
    LIST_ITEM = "list-item"
    HIDDEN = "hidden"
