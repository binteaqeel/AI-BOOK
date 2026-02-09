// @ts-check

/**
 * @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction',
    },
    {
      type: 'category',
      label: 'Part 1 — Foundations',
      collapsed: false,
      items: [
        'chapter1',
        'chapter2',
      ],
    },
    {
      type: 'category',
      label: 'Part 2 — RAG Chatbots',
      collapsed: false,
      items: [
        'chapter3',
        'chapter4',
      ],
    },
  ],
};

export default sidebars;
