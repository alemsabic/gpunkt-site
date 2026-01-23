import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "gpunkt",
    pageTitleSuffix: "Sprache ohne Filter. Wenn Wörter aufregen.",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "de-DE",
    baseUrl: "https://gpunkt.org",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "local",
      cdnCaching: true,
      typography: {
        header: "system-ui",
        body: "system-ui",
        code: "ui-monospace",
      },
      colors: {
        lightMode: {
          light: "#f9f66f", // background-color - bright yellow from screenshot
          lightgray: "rgba(0, 0, 0, 0.15)", // subtle navy tint
          gray: "#8B9DAA", // muted blue-gray
          darkgray: "#111", // medium navy
          dark: "#111", // primary text - dark navy
          secondary: "#111", // link-color - teal/cyan accent
          tertiary: "#111", // link-color (hover) - darker teal
          highlight: "rgba(77, 181, 181, 0.2)", // teal highlight
          textHighlight: "#4DB5B533",
        },
        darkMode: {
          light: "#000000", // Pitch Black
          lightgray: "#1a1a1a", // UI Background (Search, Inputs) - minimal lighter
          gray: "#eeeeee", // Muted text
          darkgray: "#eeeeee", // Secondary text
          dark: "#eeeeee", // Primary text
          secondary: "#eeeeee", // Links (Monochrome)
          tertiary: "#ffffff", // Hover
          highlight: "rgba(255, 255, 255, 0.1)", // Selection
          textHighlight: "#ffffff22",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents({
        minEntries: 4, // Only show TOC if 4+ headings (rare in atomic notes)
        maxDepth: 3,
        showByDefault: true,
        collapseByDefault: false,
      }),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
      // Citations plugin temporarily disabled due to Cloudflare build errors
      // Can be re-enabled later if needed for bibliography support
      // Plugin.Citations({
      //   bibliographyFile: "./content/bibliography.bib",
      //   suppressBibliography: false,
      //   linkCitations: false,
      //   csl: "apa",
      //   lang: "https://raw.githubusercontent.com/citation-style-language/locales/master/locales-de-DE.xml",
      //   showTooltips: true,
      //   tooltipAttribute: "data-tooltip",
      // }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      // Plugin.CustomOgImages(), // Deactivated due to font rendering error (Sept 11, 2025)
    ],
  },
}

export default config
