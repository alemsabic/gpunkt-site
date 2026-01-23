import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const Tagline: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
  return (
    <div class={classNames(displayClass, "tagline", "desktop-only")}>
      Reizwörter - die dunklen Ecken der Sprache.
    </div>
  )
}

Tagline.css = `
.tagline {
  font-size: 1rem;
  margin-top: 1rem;
  margin-bottom: 2.5rem;
  line-height: 1.1rem;
}
`

export default (() => Tagline) satisfies QuartzComponentConstructor
