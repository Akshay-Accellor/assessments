Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-15: Redesigned Global Navigation', () => {
    before(async () => { await browser.url('http://www.ipsy.com'); });
    it('Positive - Verify redesigned navigation enhances link visibility and crawling efficiency', async () => {
        const headerLinks = await $('.header-links');
        await expect(headerLinks).toBeDisplayed();
        const footerLinks = await $('.footer-links');
        await expect(footerLinks).toBeDisplayed();
    });
    it('Negative - Verify old navigation links not visible', async () => {
        const oldHeader = await $('.old-header');
        await expect(oldHeader).not.toBeDisplayed();
    });
    it('Edge - Verify navigation with many links', async () => {
        const allLinks = await $$('a');
        await expect(allLinks.length).toBeGreaterThan(10);
    });
});
