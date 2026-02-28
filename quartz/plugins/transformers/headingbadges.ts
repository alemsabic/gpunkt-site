import { QuartzTransformerPlugin } from "../types"
import { visit } from "unist-util-visit"
import { Element, Text, Root, ElementContent } from "hast"

// Matches [K], [A], [K], etc. in heading text nodes
const BADGE_RE = /(\[[A-ZÄÖÜ]\])/g

export const HeadingBadges: QuartzTransformerPlugin = () => {
  return {
    name: "HeadingBadges",
    htmlPlugins() {
      return [
        () => (tree: Root) => {
          visit(tree, "element", (node: Element) => {
            if (!["h1", "h2", "h3", "h4", "h5", "h6"].includes(node.tagName)) return

            const newChildren: ElementContent[] = []

            for (const child of node.children) {
              if (child.type !== "text") {
                newChildren.push(child)
                continue
              }

              const parts = (child as Text).value.split(BADGE_RE)

              if (parts.length === 1) {
                newChildren.push(child)
                continue
              }

              for (const part of parts) {
                if (part === "") continue
                if (/^\[[A-ZÄÖÜ]\]$/.test(part)) {
                  newChildren.push({
                    type: "element",
                    tagName: "span",
                    properties: { className: ["heading-badge"] },
                    children: [{ type: "text", value: part.slice(1, -1) }],
                  } as Element)
                } else {
                  newChildren.push({ type: "text", value: part } as Text)
                }
              }
            }

            node.children = newChildren
          })
        },
      ]
    },
  }
}
