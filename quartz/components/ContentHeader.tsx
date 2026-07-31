import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { formatDate, getDate } from "./Date"
import { FullSlug, resolveRelative } from "../util/path"

interface ContentHeaderOptions {
  /**
   * Base URL for the GitHub repository
   */
  baseUrl: string
  /**
   * Whether to show tags in the header
   */
  showTags?: boolean
}

const defaultOptions: ContentHeaderOptions = {
  baseUrl: "",
  showTags: false,
}

export default ((opts?: Partial<ContentHeaderOptions>) => {
  const options: ContentHeaderOptions = { ...defaultOptions, ...opts }

  const ContentHeader: QuartzComponent = ({ cfg, fileData, displayClass }: QuartzComponentProps) => {
    const text = fileData.text
    const tags = fileData.frontmatter?.tags

    // Check if ContentHeader should be hidden via frontmatter
    const showContentHeader = fileData.frontmatter?.showContentHeader !== false

    // Get file path for edit link
    let filePath = fileData.filePath ?? ""
    if (filePath.startsWith("content/")) {
      filePath = filePath.substring("content/".length)
    }
    const githubUrl = `${options.baseUrl}/${filePath}`

    // Only render if there's content and showContentHeader is not false
    if (!text || !showContentHeader) return null

    // Get date
    const date = getDate(cfg, fileData)
    const dateText = date ? formatDate(date, cfg.locale) : null

    return (
      <div class={classNames(displayClass, "content-header")}>
        <dl>
          {dateText && (
            <>
              <dt>Stand:</dt>
              <dd>
                <time datetime={date!.toISOString()}>{dateText}</time>
              </dd>
            </>
          )}

          {options.showTags && tags && tags.length > 0 && (
            <>
              <dt>Schlagwörter:</dt>
              <dd class="tags-inline">
                {tags.map((tag, index) => {
                  const linkDest = resolveRelative(fileData.slug!, `tags/${tag}` as FullSlug)
                  return (
                    <span key={tag}>
                      <a href={linkDest} class="internal tag-link">
                        {tag}
                      </a>
                      {index < tags.length - 1 && ", "}
                    </span>
                  )
                })}
              </dd>
            </>
          )}
        </dl>

        <a class="edit-link" href={githubUrl} target="_blank" rel="noopener noreferrer">
          Auf GitHub bearbeiten →
        </a>
      </div>
    )
  }

  ContentHeader.css = `
  .content-header {
    text-align: right;
    margin: 1rem 0 2.5rem 0;
    padding: 0.75rem 0;
    padding-right: 0;
  }

  .content-header dl {
    margin: 0;
    font-size: 1rem;
    line-height: 1.5;
    color: var(--darkgray);
  }

  .content-header dt {
    display: inline;
    margin-right: 0.5rem;
    color: var(--dark);
    opacity: 0.5;
  }

  .content-header dd {
    display: inline;
    margin: 0;
  }

  .content-header dd::after {
    content: "";
    display: block;
    margin-bottom: 0.25rem;
  }

  .content-header .tags-inline {
    display: inline;
  }

  .content-header .tags-inline a.tag-link {
    color: var(--dark);
    font-size: 0.7rem;
  }

  .content-header a.edit-link {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.85rem;
    color: var(--dark);
    opacity: 0.5;
    text-decoration: none;
    transition: opacity 0.2s ease;
  }

  .content-header a.edit-link:hover {
    opacity: 1;
    text-decoration: underline;
  }
  `

  return ContentHeader
}) satisfies QuartzComponentConstructor<ContentHeaderOptions>
